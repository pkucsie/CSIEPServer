from rest_framework.renderers import JSONRenderer
from app_api.models import Judge, Project, Track, Score


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


class MyJSONRendererScore(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        project_id = data[0]["id"]
        track_ids = []
        data_list = []
        score = Score.objects.filter(project_id=project_id)
        if score:
            for checked_object in score.all():
                track_ids.append(checked_object.id)
        else:
            project = Project.objects.get(id=project_id)
            judge = Judge.objects.get(id=2)
            score = Score.objects.create(project_id=project.id,judge_id=judge.id)
            print("score:", score)
            score.round = 1
            score.save()
            score = Score.objects.filter(project=project)
        for i in score:
            d = dict()
            d["id"] = i.id
            d["judge"] = i.judge.id
            d["project"] = i.project.id
            d["round"] = i.round
            d["innovation"] = i.innovation
            d["commercial"] = i.commercial
            d["competitiveness"] = i.competitiveness
            d["team"] = i.team
            d["public_benefit"] = i.public_benefit
            d["sum"] = i.sum
            d["comment"] = i.comment
            track_ids.append(d)

        ret_data = {'code': 0,
                    "msg": "success"}
        if data:
            ret_data["data"] = track_ids
        else:
            pass
        return super(MyJSONRendererScore, self).render(ret_data, accepted_media_type, renderer_context)


class MyJSONRendererScoreMark(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        print(data)
        dat = data[0]
        print(dat["id"])
        print(dat["round"])
        print(dat["innovation"])
        print(dat["commercial"])
        print(dat["competitiveness"])
        print(dat["team"])
        print(dat["public_benefit"])
        print(dat["comment"])
        print(dat["sum"])

        score_id = dat["id"]
        round = dat["round"]
        innovation = dat["innovation"]
        commercial = dat["commercial"]
        competitiveness = dat["competitiveness"]
        team = dat["team"]
        public_benefit = dat["public_benefit"]
        comment = dat["comment"]
        sum = innovation + commercial + competitiveness + team + public_benefit
        track_ids = []
        data_list = []

        score = Score.objects.get(id=score_id)
        score.round = round
        score.innovation = innovation
        score.commercial = commercial
        score.competitiveness = competitiveness
        score.team = team
        score.public_benefit = public_benefit
        score.sum = sum
        score.comment = comment
        score.save()
        score = Score.objects.filter(id=score_id)
        for i in score:
            d = dict()
            d["id"] = i.id
            d["judge"] = i.judge.id
            d["project"] = i.project.id
            d["round"] = i.round
            d["innovation"] = i.innovation
            d["commercial"] = i.commercial
            d["competitiveness"] = i.competitiveness
            d["team"] = i.team
            d["public_benefit"] = i.public_benefit
            d["sum"] = i.sum
            d["comment"] = i.comment
            track_ids.append(d)

        ret_data = {'code': 0,
                    "msg": "success"}
        if data:
            ret_data["data"] = track_ids
        else:
            pass
        print("ret_data:",ret_data)
        return super(MyJSONRendererScoreMark, self).render(ret_data, accepted_media_type, renderer_context)
