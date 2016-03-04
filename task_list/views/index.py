from flask.views import MethodView
from flask import render_template
from task_list import auth, db
from task_list.models import User


class IndexView(MethodView):

    decorators = [auth.login_required]

    def get(self):
        user_session = db.session.query(User).first()
        return render_template('index.html', user=user_session)
