import jenkins
from jenkins import Jenkins
from Inputs.Inputs_to_jenkinsAPI import Inputs

class View:
    def __init__(self):
        try:
            self.jenkins = Jenkins(Inputs.jenkins_url, username=Inputs.username, password=Inputs.password)
            print("Successfully connected to Jenkins.")
        except jenkins.JenkinsException as e:
            print(f"Failed to connect to Jenkins: {e}")


    def create_the_view(self,view_name):
        try:
            view_config = open('../Inputs/XMLs/sample_view.xml', mode='r', encoding='utf-8').read()
            self.jenkins.create_view(view_name,view_config)
            print("Created a new view in jenkins...")
        except jenkins.JenkinsException as e:
            print(f"failed to create a view : {e}")

    def get_all_view_names(self):
        try:
            views = self.jenkins.get_views()
            print(f"Available views in jenkins are :")
            for view in views:
                print(f" - {view['name']}")
        except jenkins.JenkinsException as e:
            print(f"failed to fetch views : {e}")

    def update_the_view(self,update_view_name):
        try:
            updated_view_config = open('../Inputs/XMLs/updated_job_view.xml', mode='r', encoding='utf-8').read()
            self.jenkins.reconfig_view(update_view_name,updated_view_config)
            print(f"updated the {update_view_name} successfully")
        except jenkins.JenkinsException as e:
            print(f"failed to update {update_view_name} : {e}")


    def delete_the_view(self,delete_view_name):
        try:
            self.jenkins.delete_view(delete_view_name)
            print(f"deleted the {delete_view_name} successfully")
        except jenkins.JenkinsException as e:
            print(f"failed to delete {delete_view_name} : {e}")



if __name__ == '__main__':
    view = View()
    view.create_the_view('My View')
    view.create_the_view('My new View')
    view.get_all_view_names()
    view.update_the_view('My View')
    view.delete_the_view('My new View')
    view.get_all_view_names()


