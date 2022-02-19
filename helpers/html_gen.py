from helpers import db

from config.config import enable_minification


minify =  enable_minification and "min." or ""


# This is the base of all pages.
# In which the content is wrapped.
async def boilerplate(content):
	return f"""
	<!DOCTYPE html>
	<html lang="en">
	<meta charset="utf-8" />
	<title>Rws.</title>
	<link href="../static/style/style.{minify}css" rel="stylesheet" />
	<body>
	  <nav>
	    <ul>
	      <li id="logo"><a href="/">R</a></li>
	      <li><a href="#">Top</a></li>
	      <li><a href="#">New</a></li>
	      <li id="login"><a href="#">Login</a></li>
	    </ul>
	  </nav>
	  {content}
	  <footer>
	    <span><a href="#">Privacy policy</a></span>
	    <span><a href="#">About us</a></span>
	  </footer>
	  </div>
	</body>
	<script type="module" src="../static/script/main.{minify}js" defer></script>
	</html>
	"""


# Build the post items.
async def posts():
	posts = ""
	for post in await db.posts():
		posts += f"""
		<div class="post">
		  <a class="title" href="">{post["title"]}</a>
		  <span class="meta">
		  	<span>by </span><a href="#" class="author">{post["author"]}</a>
		  	<span class="time" data-timestamp="{post["time"]}"></span>
		  	<a href="#" class="tag">{post["tag"]}</a>
		  </span>
		  <span class="actions">
		  	<a href="#" class="comments">{post["n_replies"]} comments</a>
		  	|
		  	<a href="#" class="share">share</a>
		  	|
		  	<a href="#" class="hide">hide</a>
		  </span>
		</div>
		"""
	return f"<div id = 'posts'>{posts}</div>"


async def homepage():
	p = await posts()
	page = await boilerplate(p)
	return page
