from datetime import datetime
class Stats(object):
    def __init__(self,command,id):
        self.command=command
        self.id=id
        self.response=None
        self.start_time=datetime.now()
        self.end_time=None
        self.duration=None
    def add_reponse(self,response):
        self.response=response
        self.end_time=datetime.now()
        self.duration=get_duration()
        
    def get_duration(self):
        diff=self.end_time-self.start_time
        return diff.total_seconds()

    def print_stat(self):
        print(f'\nid: {self.id}')
        print(f'\ncommand: {self.command}')
        print(f'\nresponse: {self.response}')
        print(f'\nstart time: {self.start_time}')
        print(f'\nend time: {self.end_time}')
        print(f'\nduration: {self.duration}')

    def grab_response(self):
        if self.response==None:
            return False
        else:
            return True

    def return_stats(self):
        str=""
        str+=(f'\nid: {self.id}\n')
        str+=(f'command: {self.command}\n')
        str+=(f'response: {self.response}\n')
        str+=(f'start time: {self.start_time}\n')
        str+=(f'end time: {self.end_time}\n')
        str+=(f'duration: {self.duration}\n')
        return str