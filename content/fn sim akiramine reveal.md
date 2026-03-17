Title: Devlog: A New Bonus Feature in v8?
Date: 2022-1-2
Tags: nightshade, devlog, FN, sim akiramine

While I've tried to spend the last few months weaning myself off overworking on my writing to avoid burnout (thus the delays to v8 and my other projects), I've still done a lot of tinkering with Python and Ren'Py. Recently, that tinkering resulted in something that I almost feel could be worth expanding into a bonus feature for Flowering Nightshade.

The working title: "**Sim Akiramine**". It's a simple dating sim that features the characters from Flowering Nightshade, allowing the player to pair off characters that may not get much screentime together otherwise. (Or just "continue" the stories of existing couples...)

Here's how it works (as of right now):

After starting the dating sim via the side stories menu, the player picks a character to play as. This list includes every character in the game, even the side stories. (So if you wanted to play as Yae, you can do so.) After that, the player spends each turn performing activities (to raise stats) or going on dates (to improve relationships).

<img alt="Status Screen" src="/images/posts/fnv8sa1.png">

The stats that can be raised are:

- **Hobbies**; represents how well the character can entertain herself and others
- **Devotion**; represents the character's ability to commit in the long term
- **Humor**; represents the character's ability to keep positive

Each character's relationship to the main character is split into two parts:

- **Friendship**; represents how well the two characters get along and enjoy their time together, 4 ranks, tied to Hobbies stat
- **Attraction**; represents how physically/romantically interested the characters are in each other, 3 ranks, tied to Devotion stat

During a turn, the player can check their stats/relationships, view potential activities and dates, and change who they want to spend the next date with. Each character also has certain preferences, which can impact how effective certain activities can be when playing as or dating that character. After raising their relationship with a character, the player can choose to start an official relationship with that character, which ties into the next point...

<img alt="Monthly Summary" src="/images/posts/fnv8sa2.png">

After every 10 turns (representing about a month), the player gets a summary of how their official relationship is going, based on the current relationship ranks. Whether or not the player character is dating anyone, this is also when stats and relationships will slightly degrade. Stats will not reduce past a certain threshold, but relationships can eventually deteriorate to 0%. This means there is always something to do, but also requires rebuilding relationships if they slip down too low.

<img alt="Confessing to Himeka" src="/images/posts/fnv8sa3.png">

Another mechanic that is being considered is to have mini-events whenever the player first reaches a new relationship rank with a character, or first starts dating her. The scenes have to be fairly short and generic due to the number of potential pairings, but hopefully it's better than having it solely be a numbers game. (If this works well, maybe more mini-events could be slipped in somewhere...)

Aside from a lack of art assets and mini-event text, the basic structure of the game is fairly complete. The real question is, would anyone find it fun enough to want to play? If it were to be included in v8 (or any future release of Flowering Nightshade), would people enjoy it?

That's all I have to show for now, so thanks for reading. (More side stories are still planned for v8/v9, but there's no news relating to those yet.) If you have opinions on whether the feature should be included in a public release, let me know what you think in the comments!