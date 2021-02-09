import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryVipGuest(params) {
  return request('/api/xadmin/v1/vip_guest', {
    params,
  });
}
export async function removeVipGuest(params) {
  return request(`/api/xadmin/v1/vip_guest/${params}`, {
    method: 'DELETE',
  });
}
export async function addVipGuest(params) {
  let fileFieldList = ["avatar"]
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/vip_guest', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateVipGuest(params, id) {
  let fileFieldList = ["avatar"]
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/vip_guest/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryVipGuestVerboseName(params) {
  return request('/api/xadmin/v1/vip_guest/verbose_name', {
    params,
  });
}
export async function queryVipGuestListDisplay(params) {
  return request('/api/xadmin/v1/vip_guest/list_display', {
    params,
  });
}
export async function queryVipGuestDisplayOrder(params) {
  return request('/api/xadmin/v1/vip_guest/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

