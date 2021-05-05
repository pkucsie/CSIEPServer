from rest_framework.renderers import JSONRenderer
from app_api.models import Judge, Project, Track


class MyJSONRendererP(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        project_id = data[0]["id"]
        track_ids = []
        judge_projects = Judge.objects.get(id=project_id)
        for checked_object in judge_projects.track.all():
            track_ids.append(checked_object.id)
        data_p = Project.objects.filter(project_track__in=track_ids)
        d_list = []
        for i in data_p:
            d = dict()
            d["id"] = i.id
            d["project_name"] = i.project_name
            d["project_group_type"] = i.project_group_type
            d["project_leader_name"] = i.project_leader_name
            d["project_phone"] = i.project_phone
            d["project_introduction"] = i.project_introduction
            d["project_track_id"] = i.project_track.id
            d_list.append(d)

        ret_data = {'code': 0,
                    "msg": "success"}
        if data:
            ret_data["data"] = d_list
        else:
            pass
        return super(MyJSONRendererP, self).render(ret_data, accepted_media_type, renderer_context)


class MyJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        ret_data = {'code': 0,
                    "msg": "success"}
        if data:
            ret_data["data"] = data
        else:
            pass
        return super(MyJSONRenderer, self).render(ret_data, accepted_media_type, renderer_context)