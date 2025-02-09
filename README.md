# project-netizen
One place for Kpop fans to look at news sentiment in Korea. News related to the Korean entertainment industry currently falls within 2 categories, aggregators like reddit.com and 
netizenbuzz.blogspot or actual content creators like allkpop.com 

project-netizen's goals are to use the powers of AI to give people who are interested in Korean media to get real-time news feed.

Stack -

Frontend: Typescript
Backend: PostgreSQL, (Not sure what to combine with Typescript)
Cloud: Not decided
Potentially looking at Redis for caching.

Mistakes / things I learned:
1. Working in Chunk/Modularity 2.09.2025:
Initially, I was building out the scraper and testing this by using an actual news article and then passing thru to TS with Json. I didn't understand really the how the API or TS worked but regardless was able to get text to display on a self-hosted website. I realize I didn't need to do this and once I got the general html structure of the Korean news site article I could just copy this into a text file and test the scraper by directly printing my output into the terminal. Thereby, making the coding process faster but also way more convoluted. At the point of writing this, I have no TS or React experience so I'm pretty much learning on the fly. 

Trying to learn TS and React at the same time as I'm trying to learn the Selenium framework proved to be a bit too much since I was essentially learning 3 different things at once. At the time of typing (2/9/2025) I'm finally starting to get a strong grasp on how Selenium works, my next goal is to pass this to PSql and then to the frontend.