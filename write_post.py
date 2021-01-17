from datetime import datetime
import random
import tweet_set

def make_post(imageloc):
    title = tweet_set.get_callout()
    markdown = f"""
        ---
        layout: post
        title: "{title}"
        ---

        # Superhero wears mask, saves lives

        ![person wearing mask]({imageloc} "Test")

        I hope you like it!
        """
    filename = "docs/_posts/" + str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) + ".markdown"
    with open(filename, "xb") as newpost:
        newpost.write(markdown.encode('utf8'))


    
