# https://qiita.com/ukaznil/items/e09b7899758c991ba176

VERSION=$1
function git_archive() {

    # 現在の場所
    readonly local CURR_DIR=$(\pwd)

    # gitリポジトリのroot
    readonly local REPOSITORY_DIR=$(\git rev-parse --show-toplevel 2>/dev/null)

    # gitリポジトリかチェック
    if [ -z "${REPOSITORY_DIR}" ]; then
        echo '### This is not the repository root'
        return
    fi

    # リポジトリrootにcd
    \cd ${REPOSITORY_DIR} >/dev/null

    # .gitattributesの作成（存在していなかった場合）
    readonly local GIT_ATTRIBUTES_FILENAME='.gitattributes'
    if [ ! -f ${GIT_ATTRIBUTES_FILENAME} ]; then
        {
            echo '*~ export-ignore'
            echo '.DS_Store export-ignore'
            echo '.gitignore export-ignore'
            echo "${GIT_ATTRIBUTES_FILENAME} export-ignore"
        } >${GIT_ATTRIBUTES_FILENAME}
    fi

    # リポジトリがcleanかチェック
    if [ -n "$(\git status --porcelain)" ]; then
        echo '### There are uncommited changes'
        \git status
        \cd ${CURR_DIR} >/dev/null
        return
    fi

    # ディレクトリ名取得，先頭のドットがあれば除去する
    readonly local REPOSITORY_DIRNAME=$(echo $(\basename ${REPOSITORY_DIR}) | sed s:^[\.]*::)

    # パス取得
    readonly local REPOSITORY_PARENT_DIR="${REPOSITORY_DIR}/packages"
    # readonly local REPOSITORY_PARENT_DIR=$(\dirname ${REPOSITORY_DIR})

    # ブランチ名取得
    readonly local BRANCH_NAME=$(echo $(\git symbolic-ref --short HEAD) | sed s:/:-:g)

    # hash値取得
    readonly local HASH=$(\git rev-parse --short=7 HEAD)

    # 納品!!
    echo $VERSION
    local ZIP_NAME="${REPOSITORY_PARENT_DIR}/ron_sub_jp_tools-v${VERSION}.zip"
    \git archive --format=zip --output=${ZIP_NAME} HEAD ./automatas && {
        echo '#========#'
        echo '# Result #'
        echo '#========#'
        echo "Archived this repository as ${ZIP_NAME}"
    }

    # 元の場所に戻る
    \cd ${CURR_DIR} >/dev/null
}

git_archive