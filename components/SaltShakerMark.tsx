export function SaltShakerMark({ className }: { className?: string }) {
  return (
    <svg
      viewBox="0 0 24 24"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      className={className}
      aria-hidden="true"
    >
      {/* Outline shaker, mid-shake */}
      <g
        transform="rotate(-26 9.5 13)"
        stroke="currentColor"
        strokeWidth="1.3"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        {/* Cap plate */}
        <path d="M6.5 4h6" />
        {/* Cap sides + base */}
        <path d="M7 4v2.2h5V4" />
        {/* Three holes */}
        <circle cx="8.2" cy="5.1" r="0.35" fill="currentColor" stroke="none" />
        <circle cx="9.5" cy="5.1" r="0.35" fill="currentColor" stroke="none" />
        <circle cx="10.8" cy="5.1" r="0.35" fill="currentColor" stroke="none" />
        {/* Neck */}
        <path d="M7.6 6.2h4.8v1.4H7.6z" />
        {/* Bottle body */}
        <path d="M6.8 7.6h6.4l-.55 9.6a1.7 1.7 0 0 1-1.7 1.55h-1.9a1.7 1.7 0 0 1-1.7-1.55L6.8 7.6Z" />
      </g>

      {/* Falling salt */}
      <g className="salt-sprinkle" fill="currentColor">
        <circle cx="15.2" cy="5.8" r="0.8" />
        <circle cx="17.4" cy="7.9" r="0.6" opacity="0.7" />
        <circle cx="16.1" cy="10" r="0.45" opacity="0.5" />
        <circle cx="18.6" cy="10.6" r="0.5" opacity="0.55" />
        <circle cx="17.2" cy="12.8" r="0.35" opacity="0.35" />
      </g>
    </svg>
  );
}
