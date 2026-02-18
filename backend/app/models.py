from mongoengine import Document, StringField, IntField, DateTimeField, FloatField, ListField, ReferenceField

class Company(Document):
    name = StringField(required=True)
    location = StringField()
    created_at = DateTimeField()
    updated_at = DateTimeField()

class User(Document):
    username = StringField(required=True)
    email = StringField(required=True)
    company = ReferenceField(Company)
    created_at = DateTimeField()
    updated_at = DateTimeField()

class Leave(Document):
    user = ReferenceField(User)
    start_date = DateTimeField()
    end_date = DateTimeField()
    reason = StringField()

class Task(Document):
    title = StringField(required=True)
    description = StringField()
    assigned_to = ReferenceField(User)
    due_date = DateTimeField()

class Shift(Document):
    user = ReferenceField(User)
    start_time = DateTimeField()
    end_time = DateTimeField()

class Expense(Document):
    user = ReferenceField(User)
    amount = FloatField(required=True)
    description = StringField()
    date = DateTimeField()

class Advance(Document):
    user = ReferenceField(User)
    amount = FloatField(required=True)
    description = StringField()
    date = DateTimeField()

class Training(Document):
    title = StringField(required=True)
    description = StringField()
    participants = ListField(ReferenceField(User))
    date = DateTimeField()

class Performance(Document):
    user = ReferenceField(User)
    rating = IntField()
    comments = StringField()
    date = DateTimeField()

class Notification(Document):
    user = ReferenceField(User)
    message = StringField()
    date = DateTimeField()

class Announcement(Document):
    title = StringField(required=True)
    content = StringField()
    date = DateTimeField()

class Survey(Document):
    title = StringField(required=True)
    questions = ListField(StringField())
    date = DateTimeField()

class SurveyResponse(Document):
    survey = ReferenceField(Survey)
    user = ReferenceField(User)
    responses = ListField(StringField())
