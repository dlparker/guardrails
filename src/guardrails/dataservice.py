from __future__ import annotations   # <-roleded factor that performs ference
from pathlib import Path


import json
from decimal import Decimal
from typing import Optional, ClassVar
import warnings


from sqlalchemy.types import TypeDecorator
from sqlalchemy import create_engine, Column, ForeignKey
from sqlalchemy import Boolean, Integer, Date, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import object_session
from sqlalchemy import exc as sa_exc
from sqlalchemy import event
from sqlalchemy_repr import RepresentableBase

Base = declarative_base(cls=RepresentableBase)

class Story(Base):
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    description_column = Column(String)

    _dataservice: ClassVar[Optional["DataService"]] = None   # <-- plain attribute

    def get_tasks(self):
        session = self._dataservice.Session(expire_on_commit=False)
        try:
            res = session.query(Task).filter_by(story_id=self.id).first()
        finally:
            session.close()
        return res


@event.listens_for(Story, "load")
def _inject_dataservice_on_load(target, context):
    """
    Automatically attach the owning DataService to every Story
    when it is loaded from the database.
    """
    session = object_session(target)
    if session is None:
        return

    # Find the DataService that owns this session.
    # All DataService instances use sessionmaker(bind=engine), so we can
    # walk up from the session to find the DataService via its .bind
    engine = session.get_bind()
    # In practice, only one DataService exists per process, so we keep a weak ref registry:
    if not hasattr(engine, "_dataservice_owner"):
        return
    dataservice = engine._dataservice_owner()
    if dataservice:
        target._dataservice = dataservice
    
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    description_column = Column(String)
    story_id = Column(Integer, ForeignKey("stories.id", ondelete="CASCADE"))

    _dataservice: ClassVar[Optional["DataService"]] = None   # <-- plain attribute

    def get_story(self):
        session = self._dataservice.Session(expire_on_commit=False)
        try:
            res = session.query(Story).filter_by(id=self.story_id).first()
        finally:
            session.close()
        return res
    
@event.listens_for(Task, "load")
def _inject_dataservice_on_load(target, context):
    """
    Automatically attach the owning DataService to every Task
    when it is loaded from the database.
    """
    session = object_session(target)
    if session is None:
        return

    # Find the DataService that owns this session.
    # All DataService instances use sessionmaker(bind=engine), so we can
    # walk up from the session to find the DataService via its .bind
    engine = session.get_bind()
    # In practice, only one DataService exists per process, so we keep a weak ref registry:
    if not hasattr(engine, "_dataservice_owner"):
        return
    dataservice = engine._dataservice_owner()
    if dataservice:
        target._dataservice = dataservice
    
class DataService:
    def __init__(self, ops_dir):
        self.ops_dir = Path(ops_dir)
        self.db_file = self.ops_dir / "guardrails.db"
        self.engine = create_engine(f'sqlite:///{self.db_file}')
        # ---- NEW: register this DataService as the owner of the engine ----
        import weakref
        self.engine._dataservice_owner = weakref.ref(self)
        # -----------------------------------------------------------------
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_stories(self):
        session = self.Session(expire_on_commit=False)
        try:
            return list(session.query(Story))
        finally:
            session.close()

