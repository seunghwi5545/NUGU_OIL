# NUGU_OIL
sk nugu speaker 프로젝트 
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>1. Introduction</title><style>
/* webkit printing magic: print all background colors */
html {
	-webkit-print-color-adjust: exact;
}
* {
	box-sizing: border-box;
	-webkit-print-color-adjust: exact;
}

html,
body {
	margin: 0;
	padding: 0;
}
@media only screen {
	body {
		margin: 2em auto;
		max-width: 900px;
		color: rgb(55, 53, 47);
	}
}

body {
	line-height: 1.5;
	white-space: pre-wrap;
}

a,
a.visited {
	color: inherit;
	text-decoration: underline;
}

.pdf-relative-link-path {
	font-size: 80%;
	color: #444;
}

h1,
h2,
h3 {
	letter-spacing: -0.01em;
	line-height: 1.2;
	font-weight: 600;
	margin-bottom: 0;
}

.page-title {
	font-size: 2.5rem;
	font-weight: 700;
	margin-top: 0;
	margin-bottom: 0.75em;
}

h1 {
	font-size: 1.875rem;
	margin-top: 1.875rem;
}

h2 {
	font-size: 1.5rem;
	margin-top: 1.5rem;
}

h3 {
	font-size: 1.25rem;
	margin-top: 1.25rem;
}

.source {
	border: 1px solid #ddd;
	border-radius: 3px;
	padding: 1.5em;
	word-break: break-all;
}

.callout {
	border-radius: 3px;
	padding: 1rem;
}

figure {
	margin: 1.25em 0;
	page-break-inside: avoid;
}

figcaption {
	opacity: 0.5;
	font-size: 85%;
	margin-top: 0.5em;
}

mark {
	background-color: transparent;
}

.indented {
	padding-left: 1.5em;
}

hr {
	background: transparent;
	display: block;
	width: 100%;
	height: 1px;
	visibility: visible;
	border: none;
	border-bottom: 1px solid rgba(55, 53, 47, 0.09);
}

img {
	max-width: 100%;
}

@media only print {
	img {
		max-height: 100vh;
		object-fit: contain;
	}
}

@page {
	margin: 1in;
}

.collection-content {
	font-size: 0.875rem;
}

.column-list {
	display: flex;
	justify-content: space-between;
}

.column {
	padding: 0 1em;
}

.column:first-child {
	padding-left: 0;
}

.column:last-child {
	padding-right: 0;
}

.table_of_contents-item {
	display: block;
	font-size: 0.875rem;
	line-height: 1.3;
	padding: 0.125rem;
}

.table_of_contents-indent-1 {
	margin-left: 1.5rem;
}

.table_of_contents-indent-2 {
	margin-left: 3rem;
}

.table_of_contents-indent-3 {
	margin-left: 4.5rem;
}

.table_of_contents-link {
	text-decoration: none;
	opacity: 0.7;
	border-bottom: 1px solid rgba(55, 53, 47, 0.18);
}

table,
th,
td {
	border: 1px solid rgba(55, 53, 47, 0.09);
	border-collapse: collapse;
}

table {
	border-left: none;
	border-right: none;
}

th,
td {
	font-weight: normal;
	padding: 0.25em 0.5em;
	line-height: 1.5;
	min-height: 1.5em;
	text-align: left;
}

th {
	color: rgba(55, 53, 47, 0.6);
}

ol,
ul {
	margin: 0;
	margin-block-start: 0.6em;
	margin-block-end: 0.6em;
}

li > ol:first-child,
li > ul:first-child {
	margin-block-start: 0.6em;
}

ul > li {
	list-style: disc;
}

ul.to-do-list {
	text-indent: -1.7em;
}

ul.to-do-list > li {
	list-style: none;
}

.to-do-children-checked {
	text-decoration: line-through;
	opacity: 0.375;
}

ul.toggle > li {
	list-style: none;
}

ul {
	padding-inline-start: 1.7em;
}

ul > li {
	padding-left: 0.1em;
}

ol {
	padding-inline-start: 1.6em;
}

ol > li {
	padding-left: 0.2em;
}

.mono ol {
	padding-inline-start: 2em;
}

.mono ol > li {
	text-indent: -0.4em;
}

.toggle {
	padding-inline-start: 0em;
	list-style-type: none;
}

/* Indent toggle children */
.toggle > li > details {
	padding-left: 1.7em;
}

.toggle > li > details > summary {
	margin-left: -1.1em;
}

.selected-value {
	display: inline-block;
	padding: 0 0.5em;
	background: rgba(206, 205, 202, 0.5);
	border-radius: 3px;
	margin-right: 0.5em;
	margin-top: 0.3em;
	margin-bottom: 0.3em;
	white-space: nowrap;
}

.collection-title {
	display: inline-block;
	margin-right: 1em;
}

time {
	opacity: 0.5;
}

.icon {
	display: inline-block;
	max-width: 1.2em;
	max-height: 1.2em;
	text-decoration: none;
	vertical-align: text-bottom;
	margin-right: 0.5em;
}

img.icon {
	border-radius: 3px;
}

.user-icon {
	width: 1.5em;
	height: 1.5em;
	border-radius: 100%;
	margin-right: 0.5rem;
}

.user-icon-inner {
	font-size: 0.8em;
}

.text-icon {
	border: 1px solid #000;
	text-align: center;
}

.page-cover-image {
	display: block;
	object-fit: cover;
	width: 100%;
	height: 30vh;
}

.page-header-icon {
	font-size: 3rem;
	margin-bottom: 1rem;
}

.page-header-icon-with-cover {
	margin-top: -0.72em;
	margin-left: 0.07em;
}

.page-header-icon img {
	border-radius: 3px;
}

.link-to-page {
	margin: 1em 0;
	padding: 0;
	border: none;
	font-weight: 500;
}

p > .user {
	opacity: 0.5;
}

td > .user,
td > time {
	white-space: nowrap;
}

input[type="checkbox"] {
	transform: scale(1.5);
	margin-right: 0.6em;
	vertical-align: middle;
}

p {
	margin-top: 0.5em;
	margin-bottom: 0.5em;
}

.image {
	border: none;
	margin: 1.5em 0;
	padding: 0;
	border-radius: 0;
	text-align: center;
}

.code,
code {
	background: rgba(135, 131, 120, 0.15);
	border-radius: 3px;
	padding: 0.2em 0.4em;
	border-radius: 3px;
	font-size: 85%;
	tab-size: 2;
}

code {
	color: #eb5757;
}

.code {
	padding: 1.5em 1em;
}

.code-wrap {
	white-space: pre-wrap;
	word-break: break-all;
}

.code > code {
	background: none;
	padding: 0;
	font-size: 100%;
	color: inherit;
}

blockquote {
	font-size: 1.25em;
	margin: 1em 0;
	padding-left: 1em;
	border-left: 3px solid rgb(55, 53, 47);
}

.bookmark {
	text-decoration: none;
	max-height: 8em;
	padding: 0;
	display: flex;
	width: 100%;
	align-items: stretch;
}

.bookmark-title {
	font-size: 0.85em;
	overflow: hidden;
	text-overflow: ellipsis;
	height: 1.75em;
	white-space: nowrap;
}

.bookmark-text {
	display: flex;
	flex-direction: column;
}

.bookmark-info {
	flex: 4 1 180px;
	padding: 12px 14px 14px;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}

.bookmark-image {
	width: 33%;
	flex: 1 1 180px;
	display: block;
	position: relative;
	object-fit: cover;
	border-radius: 1px;
}

.bookmark-description {
	color: rgba(55, 53, 47, 0.6);
	font-size: 0.75em;
	overflow: hidden;
	max-height: 4.5em;
	word-break: break-word;
}

.bookmark-href {
	font-size: 0.75em;
	margin-top: 0.25em;
}

.sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol"; }
.code { font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace; }
.serif { font-family: Lyon-Text, Georgia, YuMincho, "Yu Mincho", "Hiragino Mincho ProN", "Hiragino Mincho Pro", "Songti TC", "Songti SC", "SimSun", "Nanum Myeongjo", NanumMyeongjo, Batang, serif; }
.mono { font-family: iawriter-mono, Nitti, Menlo, Courier, monospace; }
.pdf .sans { font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK SC', 'Noto Sans CJK KR'; }

.pdf .code { font-family: Source Code Pro, "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC', 'Noto Sans Mono CJK KR'; }

.pdf .serif { font-family: PT Serif, Lyon-Text, Georgia, YuMincho, "Yu Mincho", "Hiragino Mincho ProN", "Hiragino Mincho Pro", "Songti TC", "Songti SC", "SimSun", "Nanum Myeongjo", NanumMyeongjo, Batang, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK SC', 'Noto Sans CJK KR'; }

.pdf .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC', 'Noto Sans Mono CJK KR'; }

.highlight-default {
}
.highlight-gray {
	color: rgb(155,154,151);
}
.highlight-brown {
	color: rgb(100,71,58);
}
.highlight-orange {
	color: rgb(217,115,13);
}
.highlight-yellow {
	color: rgb(223,171,1);
}
.highlight-teal {
	color: rgb(15,123,108);
}
.highlight-blue {
	color: rgb(11,110,153);
}
.highlight-purple {
	color: rgb(105,64,165);
}
.highlight-pink {
	color: rgb(173,26,114);
}
.highlight-red {
	color: rgb(224,62,62);
}
.highlight-gray_background {
	background: rgb(235,236,237);
}
.highlight-brown_background {
	background: rgb(233,229,227);
}
.highlight-orange_background {
	background: rgb(250,235,221);
}
.highlight-yellow_background {
	background: rgb(251,243,219);
}
.highlight-teal_background {
	background: rgb(221,237,234);
}
.highlight-blue_background {
	background: rgb(221,235,241);
}
.highlight-purple_background {
	background: rgb(234,228,242);
}
.highlight-pink_background {
	background: rgb(244,223,235);
}
.highlight-red_background {
	background: rgb(251,228,228);
}
.block-color-default {
	color: inherit;
	fill: inherit;
}
.block-color-gray {
	color: rgba(55, 53, 47, 0.6);
	fill: rgba(55, 53, 47, 0.6);
}
.block-color-brown {
	color: rgb(100,71,58);
	fill: rgb(100,71,58);
}
.block-color-orange {
	color: rgb(217,115,13);
	fill: rgb(217,115,13);
}
.block-color-yellow {
	color: rgb(223,171,1);
	fill: rgb(223,171,1);
}
.block-color-teal {
	color: rgb(15,123,108);
	fill: rgb(15,123,108);
}
.block-color-blue {
	color: rgb(11,110,153);
	fill: rgb(11,110,153);
}
.block-color-purple {
	color: rgb(105,64,165);
	fill: rgb(105,64,165);
}
.block-color-pink {
	color: rgb(173,26,114);
	fill: rgb(173,26,114);
}
.block-color-red {
	color: rgb(224,62,62);
	fill: rgb(224,62,62);
}
.block-color-gray_background {
	background: rgb(235,236,237);
}
.block-color-brown_background {
	background: rgb(233,229,227);
}
.block-color-orange_background {
	background: rgb(250,235,221);
}
.block-color-yellow_background {
	background: rgb(251,243,219);
}
.block-color-teal_background {
	background: rgb(221,237,234);
}
.block-color-blue_background {
	background: rgb(221,235,241);
}
.block-color-purple_background {
	background: rgb(234,228,242);
}
.block-color-pink_background {
	background: rgb(244,223,235);
}
.block-color-red_background {
	background: rgb(251,228,228);
}
.select-value-color-default { background-color: rgba(206,205,202,0.5); }
.select-value-color-gray { background-color: rgba(155,154,151, 0.4); }
.select-value-color-brown { background-color: rgba(140,46,0,0.2); }
.select-value-color-orange { background-color: rgba(245,93,0,0.2); }
.select-value-color-yellow { background-color: rgba(233,168,0,0.2); }
.select-value-color-green { background-color: rgba(0,135,107,0.2); }
.select-value-color-blue { background-color: rgba(0,120,223,0.2); }
.select-value-color-purple { background-color: rgba(103,36,222,0.2); }
.select-value-color-pink { background-color: rgba(221,0,129,0.2); }
.select-value-color-red { background-color: rgba(255,0,26,0.2); }

.checkbox {
	display: inline-flex;
	vertical-align: text-bottom;
	width: 16;
	height: 16;
	background-size: 16px;
	margin-left: 2px;
	margin-right: 5px;
}

.checkbox-on {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22%2358A9D7%22%2F%3E%0A%3Cpath%20d%3D%22M6.71429%2012.2852L14%204.9995L12.7143%203.71436L6.71429%209.71378L3.28571%206.2831L2%207.57092L6.71429%2012.2852Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E");
}

.checkbox-off {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20x%3D%220.75%22%20y%3D%220.75%22%20width%3D%2214.5%22%20height%3D%2214.5%22%20fill%3D%22white%22%20stroke%3D%22%2336352F%22%20stroke-width%3D%221.5%22%2F%3E%0A%3C%2Fsvg%3E");
}
	
</style></head><body><article id="8666b9e0-6b91-4556-b9b0-9ebcd02888dc" class="page sans"><header><h1 class="page-title">1. Introduction</h1><table class="properties"><tbody></tbody></table></header><div class="page-body"><h2 id="bcc5eb96-a420-4470-ba56-3094c7e0d4c2" class="">1. 프로젝트 배경 </h2><blockquote id="6c0effd7-8463-4d61-949d-a3490474c548" class="">가족들과 집콕하던 아무개씨. 내일 출근하려면 미리 주유소는 갔다와야한다. 자주 가는 주유소는 있지만, 과연 그 곳이 제일 싼게 맞을까? NUGU Speaker에서 현재 위치에서 가깝고, 가장 저렴한 순으로 정렬해서 바로 알려주면 어떨까? </blockquote><p id="a53d4f48-be2f-4d67-ae6e-50b5dc33ee51" class="">
</p><figure id="df33d5bd-88fe-4dda-8bb7-c4e99968b8bd" class="image"><a href="1%20Introduction%20df33d5bd88fe4dda8bb7c4e99968b8bd/jean-christophe-gougeon-t8bDFvkhNQY-unsplash.jpg"><img style="width:6000px" src="1%20Introduction%20df33d5bd88fe4dda8bb7c4e99968b8bd/jean-christophe-gougeon-t8bDFvkhNQY-unsplash.jpg"/></a></figure><p id="bd8b653f-1ce2-45c9-99ed-f9703258334c" class="">
</p><p id="7c98f62f-234e-43f4-b3fa-c9fe8ad9bd90" class="">NUGU 오일 서비스는 기름값을 조금이라도 줄이고자 하는 사회초년생, 자신 단골 집으로 갔으면 더 싸게 살 수 있었다고 말다툼하는 부부 혹은 친구 사이를 위해 만들어졌다. </p><p id="b30e691c-f192-42b0-98e1-484a21efd490" class="">
</p><p id="728b0156-cd6a-4b1a-854c-6355ae7998f4" class="">우리 팀이 서비스하고자하는 항목은 다음과 같다 </p><ul id="a35998ec-089a-4b70-bc31-6f5841d41aa3" class="bulleted-list"><li>사용자의 현재 위치를 기반으로 <strong>최저가 주유소</strong> 추천</li></ul><ul id="37d398d8-b49a-47c3-9fd1-23504c464bb5" class="bulleted-list"><li>해당 주유소 경유/휘발유 가격 정보 제공</li></ul><ul id="402e6fb4-7c24-48f5-b3f3-5e69bd818651" class="bulleted-list"><li> 2007년 경유/휘발유 가격부터 현재까지의 가격을 수집해 다음주 예측 가격 정보 제공 </li></ul><p id="464865f7-d69c-45bb-b451-6bb6ae37deea" class="">
</p><hr id="7433ad54-b303-4b00-a915-37a71b0e273e"/><h2 id="d9408c9e-de9c-4d1b-af69-1ed0e0c7d939" class="">2. 원하는 결과 </h2><p id="bcdf0d71-04bb-4e52-bdd7-fc09d990fc19" class="">사용자가 NUGU Speaker에게 최저가 주유소를 알려달라는 요청을 말하면, 해당 데이터를 서버에서 가져와 사용자에게 전달한다. 다음은 NUGU 오일 서비스를 사용할 때의 사용자와 NUGU의 대화 흐름이다. </p><p id="f35790d4-6228-42c6-ad43-e75bc2336aef" class="">
</p><hr id="e11ab216-15f4-4783-a727-7abc9cb5573c"/><p id="e3d312ac-be27-4c1e-b4a9-8108e2fff126" class="">
</p><p id="e40d4e9f-f48f-4b63-8fab-c2825d0944e4" class=""><strong>사용자</strong> : 아리야, 최저가 주유소 찾아줘 </p><p id="cb577aed-ce19-4952-8328-f93fea96101d" class=""><strong>NUGU</strong> : 경유를 원하시면 1번, 휘발유를 원하시면 2번을 말씀해주세요 </p><p id="0f2913aa-7c3c-48be-b43a-bb76f82f33b7" class=""><strong>사용자</strong> : 2번 </p><p id="22fc8f8d-ed5a-4789-8b7a-32516dc180bd" class=""><strong>NUGU</strong> : 반경 5km이내에 주유소 3곳을 알려드릴게요. 현대오일뱅크(주)직영 토평 1호 셀프주유소, 1387원, 푸른 주유소, 1399원, 현대오일뱅크(주)직영 토평 2호주유소, 1427원이에요 </p><p id="c926135f-aa3e-4300-b6dc-be14ac84470d" class="">
</p><hr id="e65aab26-18b9-4973-b614-f6713560c1af"/><p id="c47cb54b-07c0-4c64-82c2-5f46133ccc72" class="">
</p><p id="72c2c89d-885f-475e-93fd-f1c4c29f07d4" class="">서비스 제공을 위해 필요한 데이터셋은 다음과 같다 </p><p id="e623609b-0682-4c48-9db8-f5a808f74a88" class="">
</p><ul id="9b5f2ceb-de35-42b2-8969-93175a9d8a80" class="bulleted-list"><li><strong>유가 정보 API</strong></li></ul><p id="9f6c5650-3672-4313-b688-2ba54c73f8d4" class="">한국석유공사에서 제공하는 API로 주유소 판매 가격, 주유소 위치, 부가 서비스 등 전국 주유소 정보 및 평균 유가를 제공한다</p><figure id="f7955f69-8ba7-4490-9e70-7c674ebabd28" class="image"><a href="1%20Introduction%20df33d5bd88fe4dda8bb7c4e99968b8bd/_2020-11-28__11.29.57.png"><img style="width:2872px" src="1%20Introduction%20df33d5bd88fe4dda8bb7c4e99968b8bd/_2020-11-28__11.29.57.png"/></a></figure><p id="3f8c1af5-26a0-4c6f-a9c9-65ed78f54b32" class="">사진 출처 : <a href="http://www.opinet.co.kr/user/main/mainView.do">http://www.opinet.co.kr/user/main/mainView.do</a></p><p id="0f76d921-320d-4838-9339-f447e942b854" class="">
</p><h2 id="b46c0379-3fcd-4254-9aa6-17ac7e507957" class="">3. 서비스 flow </h2><p id="ce663fbd-c288-482e-a28e-25298642400c" class="">NUGU 오일의 서비스 구조는 다음과 같다.</p><figure id="461f4184-d761-4b9c-a0e4-62a825c2ea30" class="image"><a href="1%20Introduction%20df33d5bd88fe4dda8bb7c4e99968b8bd/Untitled.png"><img style="width:2626px" src="1%20Introduction%20df33d5bd88fe4dda8bb7c4e99968b8bd/Untitled.png"/></a></figure><p id="a3d2c1a4-669b-4cf4-9052-3efc939b5d5c" class=""> 자세한 내용은 다음 포스팅에서 확인할 수 있다. </p><p id="0202eefb-7c74-43a8-acc6-1e9ca8d755f0" class="">
</p><p id="97fb9eba-0b3b-439d-aea9-2cea3ca87805" class="">
</p><p id="31c4b2d2-392b-4027-a6ec-4ab17784af46" class="">Photo by <a href="https://unsplash.com/@alien_crafted?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Jean-christophe Gougeon</a> on <a href="https://unsplash.com/s/photos/gas-station?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></p></div></article></body></html>
