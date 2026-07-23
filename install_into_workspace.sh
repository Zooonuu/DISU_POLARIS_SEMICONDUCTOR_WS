#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="${1:-$HOME/DISU_POLARIS_WS/DISU_WS}"

mkdir -p "$TARGET"
cp -a "$SCRIPT_DIR"/. "$TARGET"/
rm -f "$TARGET/install_into_workspace.sh"

echo "프로젝트 파일을 설치했습니다: $TARGET"
echo "다음 명령:"
echo "  cd \"$TARGET\""
echo "  code ."
echo "  bash 01_environment/setup_python.sh"
