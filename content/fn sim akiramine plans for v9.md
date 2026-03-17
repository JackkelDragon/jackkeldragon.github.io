Title: Devlog: Sim Akiramine Revisions Planned for v9
Date: 2023-2-26
Tags: nightshade, devlog, FN, sim akiramine

I've been having a difficult time trying to get back into writing lately, but this past week I had a number of ideas to try to make Flowering Nightshade's bonus mode "Sim Akiramine" more fun and easier to create content for. I thought it might be interesting to share some of the details of what is going to be changed about the mode when v9 eventually comes out.

Firstly, the nerdy part that most people won't see the effects of: I refactored a lot of the code that is used to initialize objects for Sim Akiramine, allowing some data to be created from spreadsheets instead of being hard-coded and making it possible to translate the chat and mini-event dialogue. Most of the ramifications of these changes won't ever be seen by players, but it will hopefully make it easier to create content for the mode going forward. (In fact, I could theoretically make a stand-alone game with this as a framework now, if I wanted to make a full-on dating sim.)

As for what players will see when v9 comes out, the big theme for these updates is creating and showing unique content for each character. I'm trying to fill out the chat dialogue for the characters that didn't have many lines in v8, and I think I was able to make it easier to see all of the different chat lines that are available at a specific relationship level (rather than having it be fully random). The chat menu also allows the player to re-play previously seen mini-events as well, so you don't have to start a new playthrough to see those events again.

<img alt="Revised Main Screen" src="/images/posts/fnv9sa1.png">

Next, the way the player decides how to use their time slots has been changed to make it easier to maintain stats and relationships without needing to swap back and forth. Now the player picks a personal activity for their character, then decides to do that alone (bonus stat growth) or spend time with the current partner character. Combined with that, the date activities have been modified a bit so that the options are more relevant to the characters involved. (For instance, either the player or the partner must be Izumi or Kiyomi in order to have the option to "Go Jogging".) Likes and dislikes are still part of the game, though, so just because it's on the list doesn't mean it's a good option. (Also, stat degradation at the end of each month may be slightly tweaked to account for the boost to stat growth in this new setup.)

The last major update so far is the expansion of the monthly summaries to have character-specific variants. While most of the summaries that exist in v8 are still present, certain relevant summaries based on the player character and (if applicable) their girlfriend are now in the game, and they are weighted slightly so they have a higher chance of appearing than generic summaries.

<img alt="Unique Monthly Summary" src="/images/posts/fnv9sa2.png">

Aside from all of that, there have also been some attempts to clean up the UI a bit, but we'll see how that goes. It seems whenever I fix one version of the UI (PC or mobile), the other one finds a way to break something...

And that's all of the changes that have been made so far, more or less. For those who read this far, are any of these sounding particularly exciting? (Does anyone even play this mode?) What sort of additional features would you be interested in seeing appear in Sim Akiramine? Personally, some ideas I've considered but haven't figured out how to implement are:

- A way to show the PC talking a bit, even if not as extensively as the partners/love interests. But where would this be done? (How the character thinks about themselves is already in the single monthly summaries. Including them in mini-events would be a quick way to make a lot of awkward dialogue that clearly is just lines of texts slapped together, due to the number of character combinations.)
- A loyalty/prestige value of some kind, where overfilling the relationship meters for a character would build up this value, which never degrades. But what would it unlock? (More events? That's more dialogue to write. New outfits? That's more art to commission.) Would there be a hard cap, or would there need to be a way to "infinitely" increase the value without breaking the UI?
- Custom chibis for certain date types. But with how expensive it could become, there would have to be limits to which chibi sets were made. Aside from casual/work/swimsuit designs, I'm not sure what would be interesting and affordable.

At any rate, thanks for reading! Version 9 is still a ways off (due to the story not being written yet), but I hope people look forward to the updates!