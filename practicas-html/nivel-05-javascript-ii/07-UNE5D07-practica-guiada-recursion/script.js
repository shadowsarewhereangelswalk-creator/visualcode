const project = {
  name:"mi-aplicacion",
  children:[
    {name:"index.html"},
    {name:"assets", children:[
      {name:"styles", children:[{name:"main.css"},{name:"responsive.css"}]},
      {name:"scripts", children:[{name:"app.js"},{name:"storage.js"}]},
      {name:"images", children:[{name:"logo.svg"}]}
    ]},
    {name:"README.md"}
  ]
};
const tree = document.querySelector("#folder-tree");
const summary = document.querySelector("#tree-summary");
const renderButton = document.querySelector("#render-tree");
const expandButton = document.querySelector("#expand-tree");
const collapseButton = document.querySelector("#collapse-tree");
let nodeCount = 0;

function renderNode(node) {
  nodeCount += 1;
  const item = document.createElement("li");
  if (!node.children) {
    item.className = "file";
    item.textContent = node.name;
    return item;
  }
  const details = document.createElement("details");
  const heading = document.createElement("summary");
  const list = document.createElement("ul");
  heading.textContent = node.name;
  node.children.forEach(child => list.append(renderNode(child)));
  details.append(heading, list);
  item.append(details);
  return item;
}

function renderTree() {
  tree.replaceChildren();
  nodeCount = 0;
  tree.append(renderNode(project));
  summary.textContent = "La recursión procesó " + nodeCount + " nodos.";
}

renderButton.addEventListener("click", renderTree);
expandButton.addEventListener("click", () => document.querySelectorAll("details").forEach(detail => detail.open = true));
collapseButton.addEventListener("click", () => document.querySelectorAll("details").forEach(detail => detail.open = false));
renderTree();
