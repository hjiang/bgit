(require [hy.contrib.walk [let]])
(import [git [Repo]]
        [git.exc [InvalidGitRepositoryError]]
        argparse)

(defn read-repo-paths [] ["~/bin" "~/org" "~/.config" "~/.doom.d"])

(defn show-status []
  (for [path (read-repo-paths)]
    (try
      (let [repo (Repo path)]
        (if (.is_dirty repo)
            (print path "(dirty)")
            (print path "(clean)")))
      (except [InvalidGitRepositoryError]
        (print path "(invalid)")))))

(defn main []
  (let [argp (argparse.ArgumentParser :description "Manage multiple git repos")]
    (.add-argument argp "command" :nargs "?" :help "what action to take" :default "help")
    (let [args (.parse_args argp)]
      (cond [(= args.command "status") (show-status)]
            [True (.print-help argp)]))))

(if (= __name__ "__main__")
    (main))
