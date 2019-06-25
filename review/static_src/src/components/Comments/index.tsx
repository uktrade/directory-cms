import * as React from 'react';
import * as dateFormat from 'dateformat';

import APIClient from '../../api';
import { Comment, Store, State } from '../../state/comments';
import WagtailReactModal from '../WagtailReactModal';

interface CommentsProps extends State {
    api: APIClient;
    store: Store;
}

export default class Comments extends React.Component<CommentsProps> {
    renderComment(comment: Comment): React.ReactFragment {
        return (
            <>
                <div className="comment__header">
                    <div className="comment__header-info">
                        <h2>{comment.author.name}</h2>
                        <p className="comment__date">
                            {dateFormat(comment.date, 'h:MM mmmm d')}
                        </p>
                    </div>
                    <div className="comment__header-resolved">
                        <label htmlFor="resolved">Resolved</label>
                        <input
                            name="resolved"
                            type="checkbox"
                            checked={comment.isResolved}
                            disabled={true}
                        />
                    </div>
                </div>
                <p className="comment__text">{comment.text}</p>
            </>
        );
    }

    render() {
        let { isOpen, comments } = this.props;

        let commentsRendered = comments.map(comment => {
            return <li key={comment.id}>{this.renderComment(comment)}</li>;
        });

        return (
            <WagtailReactModal isOpen={isOpen} contentLabel="Comments">
                <div className="comments">
                    <ul>{commentsRendered}</ul>
                </div>
            </WagtailReactModal>
        );
    }
}
