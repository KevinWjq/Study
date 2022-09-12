from dataclasses import asdict
from geektime.service.petclinic.api.owner import Owner
from geektime.service.petclinic.framework.http import Request
from geektime.service.petclinic.utils.log import log


class Owners:
    '''def list(self, lastName) -> list[Owner]:'''
    def list(self, lastName):
        # r = requests.get(
        #     'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners',
        #     params={'lastName': lastName}
        # )

        request = Request()
        request.method = 'get'
        # request.host = 'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com'
        request.path = '/petclinic/api/owners'
        request.query = {'lastName': lastName}
        r = request.send()

        if r.status_code == 200:
            owner_list = []
            for item in r.json():
                owner = Owner(**item)
                owner_list.append(owner)
                log.debug(owner_list)
            return owner_list
        else:
            return []

    def add(self, owner):
        # r = requests.post(
        #     url='https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners',
        #     json=asdict(owner)
        # )

        request = Request()
        request.method = 'post'
        # request.host = 'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com'
        request.path = '/petclinic/api/owners'
        request.data = asdict(owner)
        r = request.send()

        return r

    def update(self, Owner):
        ...

    def delete(self, owner_id):
        # r = requests.request(
        #     'delete',
        #     f'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners/{owner_id}'
        # )

        request = Request()
        request.method = 'delete'
        request.host = 'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com'
        request.path = f'/petclinic/api/owners/{owner_id}'
        r = request.send()
        return r

    def clear(self, lastName):
        for item in self.list(lastName):
            self.delete(item.id)
