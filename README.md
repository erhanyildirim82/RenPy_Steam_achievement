# RenPy_Steam_achievement
How to add Steam achievements to your Renpy game

Unlocking achievements in life is hard, but in Ren'Py, it's just a few lines of code!

I've added Steam achievements to my Ren'Py game, and I wanted to share the setup in case it helps fellow developers.
🛠️ What I Did

    Configured options.rpy
        Added config.steam_appid and set up the save directory.
        Steam now knows my game exists (which is a good start!).

    Created achievements.rpy
        Initialized Steam API.
        Registered achievements.
        Synced everything so Steam doesn’t forget my hard-earned victories.

📂 Files in This Repo

    options.rpy → Steam App ID and save directory setup.
    achievements.rpy → Achievement registration and syncing.

🚀 How to Use

    Copy these files into your Ren'Py project.
    Replace my achievement names with your own (or don’t, if you like my naming style).
    Make sure the achievement API IDs match what’s in Steamworks.
    Profit.

Feel free to use, modify, or improve it. If your game has cooler achievements than mine, I’m both impressed and jealous. 😄


Steam Achievements Checklist ✅

Before pushing your game to Steam, make sure you've checked off everything:

✔️ Steamworks SDK Integration

Ensure steam_api.dll (Windows) or libsteam_api.so (Linux/Mac) is in the correct folder.

✔️ Achievements Are Registered in Steamworks

Go to Steamworks Dashboard > Achievements and add the achievement IDs (ACH_EP1_COMP, etc.).

✔️ Unlock Calls Are Implemented

Use achievement.unlock("ACH_ID") when a player meets the achievement condition.

✔️ Steam Overlay Test

Run the game via Steam, press Shift + Tab, and check if achievements unlock.

✔️ No Errors in Ren'Py Console

Open Ren'Py Console (Shift + O) and check for Steam API errors.


Final Notes 📝

If you're seeing issues, double-check your Steamworks setup and ensure the API is properly loaded. And if all else fails… well, at least your players will have fun without achievements! 😆

Happy coding! 🎮
