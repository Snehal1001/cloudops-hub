import { useState } from "react";

interface Props {
  onCreate: (name: string, description: string) => void;
}

function ProjectForm({ onCreate }: Props) {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    onCreate(name, description);

    setName("");
    setDescription("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Create Project</h2>

      <div>
        <input
          type="text"
          placeholder="Project Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
      </div>

      <div>
        <textarea
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
      </div>

      <button type="submit">Create</button>
    </form>
  );
}

export default ProjectForm;
