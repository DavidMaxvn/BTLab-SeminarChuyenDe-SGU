CONTEXT: Bạn sẽ nhận được các bước thao tác trên giao diện PyCharm để thực hiện một quy trình Git.

TASK: Chuyển các bước GUI đó thành các lệnh CLI tương ứng.

PROCESS: Commit và push các file mong muốn lên remote branch.

STEPS: {{{
1. Review changed files
2. Stage the desired files
3. Add a commit message
4. Commit the files
5. Validate branch name
6. Push the changes to the remote branch
}}}

CLI COMMANDS:
1. `git status` - Review changed files
2. `git add <file>` - Stage the desired files
3. `git commit -m "message"` - Add a commit message
4. `git commit` - Commit the files
5. `git branch` - Validate branch name
6. `git push origin <branch>` - Push the changes to the remote branch