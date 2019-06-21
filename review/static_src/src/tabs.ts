function createTab(text: string, onClick: (e: MouseEvent) => void) {
    let liElement = document.createElement('li');

    let aElement = liElement.appendChild(document.createElement('a'));
    aElement.href = '#';
    aElement.addEventListener('click', e => {
        e.preventDefault();
        e.stopPropagation();
        onClick(e);
    }, {capture: true});
    aElement.appendChild(document.createTextNode(text));

    return liElement;
}

interface TabConfig {
    text: string;
    onClick: () => void;
}

export function initTabs(tabs: TabConfig[]) {
    let tabsElement = document.querySelector('ul.tab-nav');
    if (!(tabsElement instanceof HTMLUListElement)) {
        console.error('[review] Cannot locate tabs element in DOM');
        return;
    }
    tabsElement.style.position = 'relative';

    let container = document.createElement('div');
    container.style.position = 'absolute';
    container.style.right = '50px';

    for (let tab of tabs) {
        container.appendChild(createTab(tab.text, tab.onClick));
    }

    tabsElement.appendChild(container);
}
