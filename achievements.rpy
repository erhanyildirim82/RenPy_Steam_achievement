# achievements.rpy or add it to another init block in your game.
init python:
    # Launch Steam API
    achievement.steam_init()

    # Başarımları tanımla
    achievement.register("ACH_EP1_COMP")
    achievement.register("ACH_EP2_COMP")
    achievement.register("ACH_EP3_COMP")
    achievement.register("ACH_EP4_COMP")
    achievement.register("ACH_EP5_COMP")
    achievement.register("ACH_EP6_COMP")

    # Define achievement variables - must be the same as API IDs in Steamworks.
    ACH_EP1_COMP = "ACH_EP1_COMP"     
    ACH_EP2_COMP = "ACH_EP2_COMP"     
    ACH_EP3_COMP = "ACH_EP3_COMP"     
    ACH_EP4_COMP = "ACH_EP4_COMP"     
    ACH_EP5_COMP = "ACH_EP5_COMP"     
    ACH_EP6_COMP = "ACH_EP6_COMP"

    # Synchronize Steam achievements.
    achievement.sync()