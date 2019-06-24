import * as React from 'react';
import * as Modal from 'react-modal';

import APIClient, { NewShareValidationError } from '../../api';
import { Store, State, Share } from '../../state';
import { hideShareModal, putShare } from '../../actions';

import './style.scss';
import dateFormat = require('dateformat');

interface ShareModalProps extends State {
    api: APIClient;
    store: Store;
}

interface ShareModalState {
    errors: NewShareValidationError | null,
}

export default class ShareModal extends React.Component<ShareModalProps, ShareModalState> {
    constructor(props: ShareModalProps) {
        super(props);

        this.state = {
            errors: null,
        };
    }

    render() {
        let onClickClose = (e: React.MouseEvent) => {
            e.preventDefault();

            this.props.store.dispatch(hideShareModal());
        };

        let onKeyDownInEmailBox = async (
            e: React.KeyboardEvent<HTMLInputElement>
        ) => {
            if (e.key == 'Enter') {
                let target = e.target;
                if (target instanceof HTMLInputElement) {
                    let newEmail = target.value;

                    this.setState({errors: null});

                    let response = await this.props.api.newShare(newEmail);

                    if (response.status == 'ok') {
                        target.value = '';
                        this.props.store.dispatch(
                            putShare(Share.fromApi(response.share))
                        );
                    } else {
                        this.setState({errors: response});
                    }
                }
            }
        };

        let renderedShares = this.props.shares.map(share => {
            return (
                <tr>
                    <td>{share.nameOrEmail}</td>
                    <td>{share.accessedAt == null ? 'Never' : dateFormat(share.accessedAt)}</td>
                    <td>{dateFormat(share.expiresAt)}</td>
                    <td>
                    </td>
                </tr>
            );
        });

        let error = <></>;
        if (this.state.errors && this.state.errors['email']) {
            error = <div className="error">
                {this.state.errors['email']}
            </div>;
        }

        return (
            <Modal
                isOpen={this.props.isShareModalOpen}
                contentLabel="Share"
                className="share-modal__dialog"
                overlayClassName="share-modal"
                onAfterOpen={() => {
                    let backdrop = document.body.appendChild(document.createElement('div'));
                    backdrop.classList.add('modal-backdrop');
                    backdrop.classList.add('in');
                }}
                onAfterClose={() => {
                    let backdrop = document.querySelector('body > div.modal-backdrop');

                    if (backdrop instanceof HTMLElement) {
                        backdrop.remove();
                    }
                }}
            >
                <div className="share-modal__content">
                    <button type="button" className="button close icon text-replace icon-cross" data-dismiss="modal" aria-hidden="true" onClick={onClickClose}>×</button>
                    <div className="share-modal__body">
                        <header className="merged tab-merged">
                            <div className="row nice-padding">
                                <div className="left">
                                    <div className="col header-title">
                                        <h1 className="icon icon-share">Share</h1>
                                    </div>
                                </div>
                            </div>
                        </header>

                        <div className="tab-content">
                            <div className="nice-padding">
                                <p></p>

                                <input
                                    type="text"
                                    placeholder="Enter email address"
                                    onKeyDown={onKeyDownInEmailBox}
                                ></input>
                                {error}

                                <table>
                                    <thead>
                                        <th>Name/email</th>
                                        <th>Last accessed</th>
                                        <th>Expires at</th>
                                        <th>Actions</th>
                                    </thead>
                                    <tbody>{renderedShares}</tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </Modal>
        );
    }
}
