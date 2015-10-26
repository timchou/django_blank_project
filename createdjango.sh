#!/bin/bash          

#源目录
EXAMPLE_DIR='/u01/www/django_blank_project/django.project'
#源项目名
EXAMPLE_NAME='djangoexample'

#目的项目目录
DEST_DIR='/u01/www/cloud'
#目的项目名
DEST_NAME='cloud'

#check if dest directory exists
if [ -d "$DEST_DIR" ]; then
    echo "dest directory $DEST_DIR exists,so exit."
    exit;
fi

#create virtual env
virtualenv $DEST_DIR

#copy files
echo "copying source files to dest..."
cp -R $EXAMPLE_DIR $DEST_DIR/$DEST_NAME.server
cd $DEST_DIR/$DEST_NAME.server
mv $EXAMPLE_NAME $DEST_NAME

#check if dest directory exists
if [ ! -d "$DEST_DIR/$DEST_NAME.server" ]; then
    echo "dest directory $DEST_DIR/$DEST_NAME.server not exists,so exit."
    exit;
fi

#replace project name
echo "replace project name..."
find $DEST_DIR/$DEST_NAME.server -type f -name '*.py' -exec sed -i '' s/djangoexample/$DEST_NAME/ {} +

#random key
echo "generate some random info..."
IDKEY=`cat /dev/urandom | env LC_CTYPE=C tr -cd 'a-f0-9' | head -c 8`
sed -i '' s/IDKEY=0x3b77db4b/IDKEY=0x$IDKEY/ $DEST_DIR/$DEST_NAME.server/$DEST_NAME/consts.py

SECRET=`cat /dev/urandom | env LC_CTYPE=C tr -cd 'a-f0-9' | head -c 32`
sed -i '' s/SECRET_KEY=\'\'/SECRET_KEY=\'$SECRET\'/ $DEST_DIR/$DEST_NAME.server/$DEST_NAME/settings.py


source $DEST_DIR/bin/activate
cd $DEST_DIR/$DEST_NAME.server/

echo "done!"
echo "then you should :"
echo "1.run :   pip install -r requirements.txt"
echo "2.create database $DEST_NAME in mysql"
echo "3.run :   python manage.py makemigrations users"
echo "4.run :   python manage.py migrate users"
echo "5.run :   python manage.py migrate"


