import xadmin
from xadmin import views
from backs.models import Classroom, Teacher, Student, Course, ClassSchedule


class BaseSetting(object):
    """
    xadmin的基础配置
    """
    enable_themes = True  # 开启主题功能
    use_bootswatch = True



class GlobalSetting(object):
    """
    设置网站标题和页脚
    """

    site_title = "课程管理系统后台管理页面"
    site_footer = "Powered By 1905C - 2020"
    menu_style = "accordion"


class ClassroomProfileAdmin(object):
    list_display = ("name", "subject")
    search_fields = ("name", "subject")
    list_filter = ("name", "subject")
    model_icon = 'fa fa-book'


class TeacherProfileAdmin(object):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)
    model_icon = 'fa fa-book'


class StudentProfileAdmin(object):
    list_display = ("name", "cls")
    search_fields = ("name", "cls")
    list_filter = ("name", "cls")
    model_icon = 'fa fa-book'


class CourseProfileAdmin(object):
    list_display = ("name", "teacher", "description")
    search_fields = ("name", "teacher", "description")
    list_filter = ("name", "teacher", "description")
    model_icon = 'fa fa-book'


class ClassScheduleProfileAdmin(object):
    list_display = ("week", "time", "cls", "courses", "teacher")
    search_fields = ("week", "time", "cls", "courses", "teacher")
    list_filter = ("week", "time", "cls",  "courses", "teacher")
    model_icon = 'fa fa-book'


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(Classroom, ClassroomProfileAdmin)
xadmin.site.register(Teacher, TeacherProfileAdmin)
xadmin.site.register(Student, StudentProfileAdmin)
xadmin.site.register(Course, CourseProfileAdmin)
xadmin.site.register(ClassSchedule, ClassScheduleProfileAdmin)
