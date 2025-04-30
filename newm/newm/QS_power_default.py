#times in seconds; one minute = 60 seconds
minute = 60
hour = 60*minute
# QS_operation: light, display_off, lock_screen, suspend, hibernate, none
energy = {
    "QS_idle_times": [minute*10, minute*15, minute*20, minute*40, hour],
    "QS_operation": {
        minute*10: "light",
        minute*15: "lock_screen",
        minute*20: "light",
        minute*40: "display_off",
        hour: "suspend",
    },
    "QS_power_value": {
        minute*10: "40%-",
        minute*20: "20%-",
    }
}
