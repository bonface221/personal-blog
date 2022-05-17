from flask import render_template,url_for,abort,redirect
from flask_login import login_required
from . import main
from .. import db
from .forms import Blog
from ..models import User,Blogs
from ..request import get_quote

@main.route('/')
def index():
  random_quote=get_quote()

  user = User.query.filter_by(username='uname').first()
  blogs = Blogs.query.all()
  title = 'Welcome to Bloggy'
  message = 'Cool Blogs'
  return render_template('index.html',random_quote=random_quote, message = message,title= title,blogs=blogs, user=user)

@main.route('/user/<uname>',methods=['GET','POST'])
@login_required
def profile(uname):
  user = User.query.filter_by(username=uname).first()
  blogs=Blogs.query.filter_by(user_id=user.id)
  if user is None:
    abort(404)
  title = f'{user.username}'
  return render_template('profile/profile.html',title=title,user = user,blogs=blogs)

@main.route('/blogs/<uname>', methods=['GET','POST'])
@login_required
def blogs(uname):
  blog_form = Blog()
  user = User.query.filter_by(username = uname).first()
  if blog_form.validate_on_submit():
    blog = Blogs(title = blog_form.title.data, description = blog_form.description.data,user = user)
    db.session.add(blog)
    db.session.commit()
    return redirect(url_for('main.index'))
  title='blogs'
  return render_template('blog.html',title=title,blog_form=blog_form)

@main.route('/blogs/delete/<int:blog_id>')
def delete(blog_id):
    blog= Blogs.query.filter_by(id=blog_id).first()
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('main.index'))