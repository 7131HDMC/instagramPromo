
from django.conf import settings
from django.core.mail import send_mail
from instagramPromoter import celery_app
from instaPrometer.scripts.BotComentarioInstagram import InstagramBot

@celery_app.task(bind=True)
def run_insta_comments_task(self, form):
  print("self.request.id")
  print(self.request.id)
  insta = InstagramBot(
    form["email"],
    form["password"],
    form["post"],
    form["max_coments"],
    form["comments_template"],
  )
  insta.login()
#   config = UserBlazeConfig.objects.get(user=user)
#   config.task_id = self.request.id
#   config.save()
#   script_run(form, self.request.id, config)
