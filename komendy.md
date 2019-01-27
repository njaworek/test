najpierw
git init
git add nazwapliku.txt
git commit -m "Komentarz do pliku"
git push -> przeniesienie na serweer


git checkout nazwa_brancha -> zmienia branch
git merge nazwia_brancha -> merguje danego brancha

sudo su -	przejscie na root

systemctl status sshd.service - sprawdzanie portow

id - sprawdzanie id

JAVA_ARGS="-Djava.awt.headless=true -Dhudson.model.DirectoryBrowserSupport.CSP=\"sandbox allow-scripts allow-same-origin; default-src 'none'; img-src 'self' data: ; style-src 'self' 'unsafe-inline' data: ; script-src 'self' 'unsafe-inline' 'unsafe-eval' ;\""

https://wiki.jenkins.io/display/JENKINS/Installing+Jenkins+on+Ubuntu


get -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update
sudo apt-get install jenkins
