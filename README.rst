===============================
Dancing With the Stars Analysis
===============================

Setup
-----

Put this in your `.bashrc` and replace the ??? with real values::

    export TWITTER_API_KEY='???'
    export TWITTER_API_SECRET='???'
    export TWITTER_ACCESS_TOKEN='???'
    export TWITTER_ACCESS_TOKEN_SECRET='???'

Then set this up::

    git clone https://github.com/audreyr/dwts-analysis.git
    mkvirtualenv dwts-analysis
    pip install -r requirements.txt

Usage
-----

Run the script::

    python dwts_followers.py

You will see the individual and combined Twitter follower counts for each of the DWTS couples in the semifinals. 