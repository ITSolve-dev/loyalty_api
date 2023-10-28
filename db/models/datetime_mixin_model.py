import sqlalchemy as sa


class DateTimeMixin(object):
    created_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.sql.func.now())
    updated_at = sa.Column(sa.DateTime, onupdate=sa.sql.func.now(), nullable=True, default=None)
