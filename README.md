# high scores

super minimal flask app for storing high scores on a server. No databases needed!

(unfortunately, can't run on Heroku or PaaS that don't have static storage)

`GET /getScores` => Return a sorted JSON list of high scores

`GET /viewScores` => HTML view of high scores

`POST /submit` (name, score, secretToken) => Adds to the highscore list. Secret token for a thin layer of security. May consider adding captcha for to prevent spambotting.

### App settings:

`LIST_SIZE` (default: 100) How many scores you want to keep, max

`SECRET_TOKEN` A token that you have to include when submitting scores to the API
