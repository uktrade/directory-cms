import * as React from 'react';
import * as ReactDOM from 'react-dom';
import * as Modal from 'react-modal';
import { createStore } from 'redux';

import ShareModal from './components/ShareModal';
import APIClient from './api';
import { reducer, Share } from './state';
import { initTabs } from './tabs';
import { showShareModal, hideShareModal, putShare } from './actions';

document.addEventListener('DOMContentLoaded', () => {
    Modal.setAppElement('div.wrapper');

    initTabs([
        {
            text: 'Share',
            onClick() {
                store.dispatch(showShareModal());
            }
        }
    ]);

    document.addEventListener('keydown', (e: KeyboardEvent) => {
        // Close share modal when esc is pressed
        if (e.key == 'Escape') {
            store.dispatch(hideShareModal());
        }
    });

    let store = createStore(reducer);
    let api = new APIClient(446);

    // Load initial shares
    api.getShares().then(shares => {
        for (let share of shares) {
            store.dispatch(putShare(Share.fromApi(share)))
        }
    });

    // Render UI
    let container = document.createElement('div');
    document.body.append(container);

    let render = () => {
        ReactDOM.render(
            <ShareModal
                api={api}
                store={store}
                {...store.getState()}
            />,
            container
        );
    };

    render();
    store.subscribe(render);
});
