# -*- coding: utf-8 -*-
db.define_table('BOOKS',
                Field('Title','string',requires=IS_NOT_EMPTY()),
                Field('Author','string',requires=IS_NOT_EMPTY()),
                Field('Book_id','integer'),
                Field('Publication','string'),
                Field('Publication_Year','integer'),
                Field('Subject_Type','string',requires=IS_NOT_EMPTY()))
                #primarykey=['Book_id'])
#db.define_table('register',
 #               Field('Name','string',requires=IS_NOT_EMPTY()),
  #              Field('Roll_no','integer',requires=IS_NOT_EMPTY()),
   #             Field('Email_id',requires=IS_EMAIL()),
    #            Field('password','password',readable=False,requires=[IS_STRONG(),CRYPT(),IS_NOT_EMPTY()],label='Password'))
db.define_table('Issued',
                 Field('Roll_No','integer',requires=IS_NOT_EMPTY()),
                 Field('Book_title','string',requires=IS_NOT_EMPTY()),
                 Field('Book_Id','integer'),
                 Field('Issue_date','datetime',default=request.now,requires=IS_DATE(format=('%d-%m-%Y')),writable=False))
               # Field('Issue_date','string'))
