Notes
=====

I was inspired by [this post](https://news.ycombinator.com/item?id=3243770) on HN, and decided that I could build my own.

This is a pretty rough first effort.

The project consists of 3 modules
---------------------------------
* jarchive - Web scraper for J-Archive. Extracts database of historical jeopardy clues/answers.
* jtextclust - Text clustering routines in R to cluster similar questions.
* jtutor - Django App to quiz players. Designed to be browser/smartphone compatible. Select questions based on learned history (optimized to get player to profitability very quickly).


Future enhancements may include
-------------------------------
* Player simulators.
* Profitability estimators.
* Per-player tracking.
* Better optimization model.
