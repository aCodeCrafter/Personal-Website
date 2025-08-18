USERNAME=""

sudo chown -R www-data:www-data .
sudo chmod -R g+w .

sudo usermod -a -G www-data $USERNAME
newgrp www-data

sudo mv personal_website_app/personal_website.service /etc/systemd/system/personal_website.service
sudo mv admin_app/admin_app.service /etc/systemd/system/admin_app.service

python3 -m venv personal_website_app/.venv && . personal_website_app/.venv/bin/activate && pip install --upgrade pip && pip install -r personal_website_app/requirements.txt && pip list && deactivate
python3 -m venv admin_app/.venv && . admin_app/.venv/bin/activate && pip install --upgrade pip && pip install -r admin_app/requirements.txt && pip list && deactivate

sudo systemctl daemon-reload && sudo systemctl restart personal_website.service && sudo systemctl restart nginx

