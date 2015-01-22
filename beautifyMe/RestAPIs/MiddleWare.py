from django.utils.functional import curry
from django.db.models import signals

class whoDidMiddleWare(object):
    
    def process_request(self, request):
        print request
        user = request.user
        mark_whodid = curry(self.mark_whodid, user)
        signals.pre_save.connect(mark_whodid,  dispatch_uid = (self.__class__, request,), weak = False)
            
    def process_response(self, request, response):
        signals.pre_save.disconnect(dispatch_uid =  (self.__class__, request,))
        return response
 
 
    def mark_whodid(self, user, sender, instance, **kwargs):
        if not getattr(instance, 'created_by', None):
            instance.created_by = user
        instance.last_updated_by = user
        



