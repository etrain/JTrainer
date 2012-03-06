Notes
=====

I was inspired by [this post](https://news.ycombinator.com/item?id=3243770) on HN, and decided that I could build my own.

This is a pretty rough first effort.

The project consists of 3 modules.
1. jarchive - Web scraper for J-Archive. Extracts database of historical jeopardy clues/answers.
2. jtextclust - Text clustering routines in R to cluster similar questions.
3. jtutor - Django App to quiz players. Designed to be browser/smartphone compatible. Select questions based on learned history (optimized to get player to profitability very quickly).

Future enhancements may include.
1. Player simulators.
2. Profitability estimators.
3. Per-player tracking.
4. Better optimization model.
