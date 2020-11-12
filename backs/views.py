from backs import serializers
from backs.models import Classroom, Teacher, Student, Course, ClassSchedule
from rest_framework.views import APIView
from rest_framework import status  # 状态码
from rest_framework.response import Response # 响应


class ClassScheduleList(APIView):
    """
    课程表get获取和post添加
    get: 返回所有课程信息
    post: 添加课程信息
    """
    def get(self, request):
        csl_set = ClassSchedule.objects.all()
        csl_data = serializers.ClassScheduleSerializer(instance=csl_set, many=True)
        return Response(csl_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        csl_data = serializers.ClassScheduleSerializer(data=request.data)
        if csl_data.is_valid():
            csl_data.save(teacher=self.request.user)
            return Response(csl_data.data, status=status.HTTP_200_OK)
        return Response(csl_data.errors, status=status.HTTP_400_BAD_REQUEST)



class ClassScheduleDetail(APIView):
    """ 课程表的查询修改和更新
    : 返回请求后的结果
    """
    @staticmethod
    def get_course(request, pk):
        try:
            return ClassSchedule.objects.get(pk=pk)
        except ClassSchedule.DoesNotExist:
            return

    def get(self, request, pk):
        course = self.get_course(request=None, pk=pk)
        if not course:
            return Response(data={"msg":"没有此课程信息"}, status=status.HTTP_400_BAD_REQUEST)
        course_data = serializers.ClassScheduleSerializer(instance=course)
        return Response(data=course_data.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        course = self.get_course(pk=pk)
        if not course:
            return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_400_BAD_REQUEST)
        course_data = serializers.ClassScheduleSerializer(instance=course, data=request.data)
        if course_data.is_valid():
            course_data.save(teacher=self.request.user)
            return Response(course_data.data, status=status.HTTP_200_OK)
        return Response(course_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = self.get_course(pk=pk)
        if not course:
            return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_400_BAD_REQUEST)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

