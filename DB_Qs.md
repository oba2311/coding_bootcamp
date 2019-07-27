# DB Qs and As:

1. What's the difference between a flush() and commit():
During a _session_ there are _transactions_ happening with the DB.
Those changed are not _commited_ initially. The session object remembers the
transaction taking place but doesn't commit those until a `session.flush()` is called.

When `session.flush()` is called, the transactions are taking place but, however,
are not written to disk. Writing to disk only happens once `session.commit()`
is called. Consequently, if `session.commit()` is called, then `session.flush()` is called automatically anyhow.

BTW: this definition `session.autoflush = True` is the default with SQLAlchemy<sup>1</sup>,
therefore changes are _flushed_ automatically as part of the session.

<sup>1</sup> SQLAlchemy [Docs](https://docs.sqlalchemy.org/en/13/orm/session_api.html):  Session and sessionmaker()


class sqlalchemy.orm.session.sessionmaker(bind=None, class_=<class 'sqlalchemy.orm.session.Session'>, **_autoflush=True_**, autocommit=False, expire_on_commit=True, info=None, **kw)
