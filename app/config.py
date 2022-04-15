class Config():
    SECRET_KEY= 'SUPER SECRET'
    #SQLALCHEMY_DATABASE_URI= 'mysql://root:Ridoco27mysql@localhost/taskapp1'
    SQLALCHEMY_DATABASE_URI= 'sqlite:///taskapp2.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False