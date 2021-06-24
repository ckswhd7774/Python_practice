from django.shortcuts import redirect, render
import boto3
from boto3.session import Session
from datetime import date, datetime
from .models import Post
from config.settings import AWS_ACCESS_KEY_ID, AWS_S3_REGION_NAME, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME


# Create your views here.
def index(request) :
    if request.method == 'POST' :
        file = request.FILES.get('img')
        session = Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_S3_REGION_NAME,
        )
        s3 = session.resource('s3')
        now = datetime.now().strftime('%Y%H%M%S')
        img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key=now+file.name,
            Body=file
        )

        s3_url = 'https://django-s3-cj.s3.ap-northeast-2.amazonaws.com/'
        Post.objects.create(
            title=request.POST['title'],
            url = s3_url+now+file.name
        )
        return redirect('index')
    posts = Post.objects.all()
    return render(request, 'index.html',{'posts':posts})