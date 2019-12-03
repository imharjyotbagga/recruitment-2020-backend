import django_filters
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin

from candidate.models import Candidate
from candidate.serializers import CandidateSerializer


# class CandidateViewSet(ModelViewSet):
# 	queryset = Candidate.objects.all()
# 	serializer_class = CandidateSerializer
#
# 	def get_permissions(self):
# 		permission_classes = []
# 		if self.action == 'create':
# 			permission_classes = [AllowAny]
# 		elif self.action == 'partial_update' or self.action == 'list' or self.action == 'retrieve':
# 			permission_classes = [IsAuthenticated]
# 		else:
# 			permission_classes = [IsAdminUser]
# 		return [permission() for permission in permission_classes]

#
# @api_view(['PATCH'])
# @permission_classes(IsAuthenticated)
# def send_email_to_candidate(request, pk):
# 	try:
# 		candidate = Candidate.objects.get(id=pk)
# 	except Candidate.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)
#
# 	if request.method == 'PATCH':
# 		try:
# 			subject = 'IEEE-VIT 2019 Recruitments'
# 			message = f"Hi, {candidate.name}! Please report to {request.user.recruiter_set.all()}"
# 			print(message)
# 			send_mail(
# 				subject=subject,
# 				message=message,
# 				from_email='jaiswalsanskar078@gmail.com',
# 				recipient_list= [candidate.email]
# 			)
# 			candidate.email_sent = True
# 		except:
# 			print('Couldn\'t send email to candidate')


class CandidateListViewset(viewsets.GenericViewSet, ListModelMixin):
    queryset = Candidate.objects.filter(called=False).order_by('timestamp')
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['room_number', 'interests']
    serializer_class = CandidateSerializer
