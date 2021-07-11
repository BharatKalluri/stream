# Thought Stream

## Idea

A telegram bot which can primarily act as a journal, with a lot more character. The bot should also ask for mood a couple of times per day, have routines setup. For example, when you go to sleep, you can trigger a routine by entering `/sleep` and the bot will log this timestamp and ask you a bunch of questions as a retrospective to the current day and finally save them further analysis. There will be many routines setup like this.

## Project status

All the responses are stored in plain text, answers to questions are in the format of a hashtag followed by a value. So, a mood recording would be `#mood 5`. This gives a lot of flexibility, but this also means that data is directly not consumable. Will have to see how this works out in the long term.

This is a personal project, I'm still evaluating how this idea will work. Although self hosting the bot is very straightforward (Its just a python bot which depends on firestore for the db).

## Inspiration

Although I had an idea of the hashtag based personal data collection and analysis and I started working on this project. I did not really know how to explain or what to collect until I got into the self quantification world. This is _really cool stuff_, do checkout the subreddit and other resources. 

- I stole the idea of config driven routine management and a bunch of really high quality questions from [FxLifeSheet](https://github.com/krausefx/fxlifesheet), huge thanks for making it open source!
- I was absoluetly mind blown by [julian.digital](https://julian.digital/), huge inspiration!
