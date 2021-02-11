import math

from pywm import PyWMView

from .state import State
from .animate import Animate, Transition

PANELS = {
    "newm-panel-notifiers": "notifiers",
    "newm-panel-launcher": "launcher"
}


class ViewState(State):
    def __init__(self, i, j, w, h):
        super().__init__(['i', 'j', 'w', 'h'])
        self.i = i
        self.j = j
        self.w = w
        self.h = h


class PresentViewTransition(Transition):
    def __init__(self, layout, view, duration, i, j, w, h):
        super().__init__(view, duration, ease=True)
        self.layout = layout
        self.view = view
        self.i = i
        self.j = j
        self.w = w
        self.h = h

    def setup(self):
        new_state = self.view.state.copy()
        new_state.i = self.i
        new_state.j = self.j
        new_state.w = self.w
        new_state.h = self.h
        super().setup(new_state)

    def finish(self):
        self.layout.reset_extent(focus_view=self.view)
        self.view.presented = True


class View(PyWMView, Animate):
    def __init__(self, wm, handle):
        PyWMView.__init__(self, wm, handle)
        Animate.__init__(self)
        self.state = ViewState(0, 0, 0, 0)
        self.client_side_scale = 1.

        self.presented = False
        self.panel = None

    def main(self):
        print("[Python] New View: %s, %s, %s, %s, floating=%s" % (self.title, self.app_id, self.role, self.is_xwayland, self.floating))
        if self.is_xwayland:
            """
            X cleints are responsible to handle
            HiDPI themselves
            """
            self.client_side_scale = self.wm.config['output_scale']

        if self.app_id in PANELS:
            self.panel = PANELS[self.app_id]
            self.set_accepts_input(False)
            self.set_z_index(6)
        else:
            self.set_z_index(0)

        if self.panel is not None:
            self.update()
            self.update_size()
            self.presented = True

        else:
            if self.floating:
                min_w, _, min_h, _ = self.size_constraints

                if (min_w, min_h) == (0, 0):
                    (min_w, min_h) = self.size

                if min_w == 0 or min_h == 0:
                    return

                ci = self.wm.state.i + self.wm.state.size / 2.
                cj = self.wm.state.j + self.wm.state.size / 2.
                if self.parent is not None:
                    ci = self.parent.state.i + self.parent.state.w / 2.
                    cj = self.parent.state.j + self.parent.state.h / 2.

                w, h = min_w, min_h
                w *= self.wm.scale / self.wm.width / self.client_side_scale
                h *= self.wm.scale / self.wm.height / self.client_side_scale

                self.state.i = ci - w / 2.
                self.state.j = cj - h / 2.
                self.state.w = w
                self.state.h = h
                
            else:
                min_w, _, min_h, _ = self.size_constraints
                min_w *= self.wm.scale / self.wm.width / self.client_side_scale
                min_h *= self.wm.scale / self.wm.height / self.client_side_scale

                self.wm.place_initial(self, max(math.ceil(min_w), 1),
                                      max(math.ceil(min_h), 1))

            i, j, w, h = self.state.i, self.state.j, self.state.w, self.state.h
            self.state.w = 0
            self.state.h = 0

            self.state.i += .5*w
            self.state.j += .5*h

            self.animation(PresentViewTransition(self.wm, self, .5, i, j, w, h))


    def update(self):
        if self.panel == "notifiers":
            self.set_box(self.wm.width * 0.4, self.wm.height * 0.7, self.wm.width * 0.2, self.wm.height * 0.3)
        elif self.panel == "launcher":
            self.set_box(self.wm.width * 0.1, self.wm.height * 0.1, self.wm.width * 0.8, 0)
        else:
            state = self.state
            wm_state = self.wm.state

            i = state.i
            j = state.j
            w = state.w
            h = state.h

            x = i - wm_state.i + wm_state.padding
            y = j - wm_state.j + wm_state.padding

            w -= 2*wm_state.padding
            h -= 2*wm_state.padding

            x *= self.wm.width / wm_state.size
            y *= self.wm.height / wm_state.size
            w *= self.wm.width / wm_state.size
            h *= self.wm.height / wm_state.size

            if self.size[0] > 0 and self.size[1] > 0:
                x -= self.offset[0] / self.size[0] * w
                y -= self.offset[1] / self.size[1] * h

            self.set_box(x, y, w, h)

    def update_size(self):
        if self.panel == "notifiers":
            self.set_size(self.box[2] * self.client_side_scale, self.box[3] * self.client_side_scale)
        elif self.panel == "launcher":
            self.set_size(self.wm.width * 0.8 * self.client_side_scale,
                          self.wm.height * 0.8 * self.client_side_scale)
        else:
            state = self.state

            width = round(state.w * self.wm.width / self.wm.scale *
                          self.client_side_scale)
            height = round(state.h * self.wm.height / self.wm.scale *
                           self.client_side_scale)

            min_w, max_w, min_h, max_h = self.size_constraints
            if width < min_w and min_w > 0:
                print("Warning: Width: %d !> %d" % (width, min_w))
            if width > max_w and max_w > 0:
                print("Warning: Width: %d !< %d" % (width, max_w))
            if height < min_h and min_h > 0:
                print("Warning: Height: %d !> %d" % (height, min_h))
            if height > max_h and max_h > 0:
                print("Warning: Height: %d !< %d" % (height, max_h))

            if (width, height) != self.size:
                self.set_size(width, height)

        self.update()

    def on_update(self):
        if self.floating and self.presented:
            """
            Keep floating windows scaled correctly
            """
            x, y, w, h = self.box
            w = self.size[0] * self.client_side_scale
            h = self.size[1] * self.client_side_scale
            self.set_box(x, y, w, h)

        if self.panel is None:
            if self.focused:
                self.set_z_index(1 + (2 if self.floating else 0))
            else:
                self.set_z_index(0 + (2 if self.floating else 0))

    def destroy(self):
        self.wm.reset_extent()
