/* @flow */

import Tools from 'src/utils/helpers/Tools';
import {FIELD_TYPE, APP} from 'src/constants';

const rawApiUrls = [
    {
        controller: 'tag',
        endpoints: {
            crud: ''
        }
    }
];

export const apiUrls = Tools.getApiUrls(rawApiUrls);

export function seeding(numberOfItems: number, single: boolean = false): any {
    let result = [];
    for (let i = 1; i <= numberOfItems; i++) {
        result.push({
            id: i,
            title: `title ${i}`,
            uid: `title-${i}`,
            checked: false
        });
    }
    if (!single) return result;
    return result[numberOfItems - 1];
}

export type FormValues = {
    id: number,
    uid: string,
    title: string
};

export const defaultFormValues: FormValues = {
    id: 0,
    uid: '',
    title: ''
};

export type FormValuesWithCheck = FormValues & {
    checked: boolean
};
