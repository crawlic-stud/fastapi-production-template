from starlette_admin.contrib.sqlmodel import ModelView

from tables.user import SuperUser


class UserView(ModelView):
    exclude_fields_from_list = [SuperUser.hashed_password]
