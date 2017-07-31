from boto.mturk.connection import MTurkConnection
from boto.mturk.question import AnswerSpecification, SelectionAnswer
from boto.mturk.question import Question, QuestionContent, QuestionForm
from boto.mturk.question import FormattedContent, Overview

import better_exceptions


# Security Credentials
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

HOST = 'mechanicalturk.sandbox.amazonaws.com'

# Making the connection
mtc = MTurkConnection(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, host=HOST, debug=1)

questions = []
answers = []

# Question 1
questionContent = QuestionContent()
questionContent.append_field('Title', 'What is your favorite car?')
questionContent.append(
    FormattedContent('<p> Make sure to think this through! </p>')
)
questionAnswer = AnswerSpecification(SelectionAnswer(
    min=1,
    max=1,
    style='radiobutton',
    selections=[
        ('Honda', 0),
        ('Toyota', 1),
        ('Hyundai', 2)
    ],
))
questions.append(Question(
    identifier='q1',
    content=questionContent,
    answer_spec=questionAnswer,
    is_required=True,
))
answers.append("""
    <Question>
        <QuestionIdentifier>q1</QuestionIdentifier>
        <AnswerOption>
            <SelectionIdentifier>0</SelectionIdentifier>
            <AnswerScore>50</AnswerScore>
        </AnswerOption>
        <AnswerOption>
            <SelectionIdentifier>1</SelectionIdentifier>
            <AnswerScore>50</AnswerScore>
        </AnswerOption>
        <AnswerOption>
            <SelectionIdentifier>2</SelectionIdentifier>
            <AnswerScore>50</AnswerScore>
        </AnswerOption>
    </Question>
""")

# Question 2
questionContent = QuestionContent()
questionContent.append_field(
    'Title',
    'What is your gender?'
)
questionAnswer = AnswerSpecification(SelectionAnswer(
    min=1,
    max=1,
    style='radiobutton',
    selections=[
        ('Male', 0),
        ('Female', 1),
    ],
))
questions.append(Question(
    identifier='q2',
    content=questionContent,
    answer_spec=questionAnswer,
    is_required=True,
))
answers.append("""\
    <Question>
        <QuestionIdentifier>q2</QuestionIdentifier>
        <AnswerOption>
            <SelectionIdentifier>0</SelectionIdentifier>
            <AnswerScore>50</AnswerScore>
        </AnswerOption>
        <AnswerOption>
            <SelectionIdentifier>1</SelectionIdentifier>
            <AnswerScore>50</AnswerScore>
        </AnswerOption>
    </Question>
""")

# Make the overall question form
testForm = QuestionForm()
overview = Overview()
overview.append_field('Text', 'Basic Demographic Information')
testForm.append(overview)
for q in questions:
    testForm.append(q)

# Make the answer key XML

AnswerKey = '<AnswerKey xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/AnswerKey.xsd">'
AnswerKey += ''.join(answers)
AnswerKey += """
    <QualificationValueMapping>
        <PercentageMapping>
            <MaximumSummedScore>100</MaximumSummedScore>
        </PercentageMapping>
    </QualificationValueMapping>
</AnswerKey>
"""

description = 'My HITS require to complete this qualification test'

print(AnswerKey);

response = mtc.create_qualification_type(name='ProjectTest1',
                              description=description,
                              status='Active',
                              keywords=['memes', 'fun'],
                              test=testForm,
                              answer_key= AnswerKey,
                              test_duration=3600);

# Prints the type id of qualification
print(response);

