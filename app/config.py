class Config():
    SECRET_KEY= 'SUPER SECRET'
    # config para conectar mysql
    #SQLALCHEMY_DATABASE_URI= 'mysql://root:Ridoco27mysql@localhost/taskapp1'
    # config para conectar sqlite3
    SQLALCHEMY_DATABASE_URI= 'sqlite:///taskapp2.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False