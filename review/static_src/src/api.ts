export interface ReviewerApi {
    name: string,
}

export interface ShareApi {
    id: number,
    reviewer: ReviewerApi
    shared_by: string,
    shared_at: string,
    first_accessed_at: string | null,
    last_accessed_at: string | null,
    expires_at: string,
}

export interface NewShareSuccess {
    status: 'ok',
    share: ShareApi,
}

export interface NewShareValidationError {
    status: 'error',
    email?: string,
}

export type NewShareResponse = NewShareSuccess | NewShareValidationError;

export default class APIClient {
    pageId: number;

    constructor(pageId: number) {
        this.pageId = pageId;
    }

    async getShares(): Promise<ShareApi[]> {
        let response = await fetch(`/admin/api/review/page/${this.pageId}/shares/`, {
            credentials: 'same-origin'
        });

        return response.json();
    }

    async newShare(email: string): Promise<NewShareResponse> {
        let response = await fetch(`/admin/api/review/page/${this.pageId}/shares/`, {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email,
            })
        });

        if (response.status == 201) {
            return {
                status: 'ok',
                share: await response.json(),
            };
        } else if (response.status == 400) {
            return {
                status: 'error',
                ...await response.json(),
            };
        } else {
            throw new Error(`share api returned unexpected status code: ${response.status}`);
        }
    }
}
